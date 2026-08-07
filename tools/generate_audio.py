"""Generate the original music and sound effects used by the game."""

from array import array
import math
import os
import random
import wave


SR = 22050
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BGM_DIR = os.path.join(ROOT, "game", "audio", "bgm")
SFX_DIR = os.path.join(ROOT, "game", "audio", "sfx")


def midi(note):
    return 440.0 * (2.0 ** ((note - 69) / 12.0))


def add_tone(buf, start, duration, note, volume, voice="piano"):
    begin = int(start * SR)
    length = min(int(duration * SR), len(buf) - begin)
    if length <= 0:
        return
    frequency = midi(note)

    for i in range(length):
        t = i / SR
        phase = 2.0 * math.pi * frequency * t
        attack = min(1.0, t / 0.025)
        release = min(1.0, (duration - t) / 0.10)
        envelope = max(0.0, attack * release)

        if voice == "piano":
            envelope *= math.exp(-2.2 * t / max(duration, 0.01))
            sample = math.sin(phase) + 0.34 * math.sin(2 * phase) + 0.12 * math.sin(3 * phase)
        elif voice == "bell":
            envelope *= math.exp(-3.0 * t / max(duration, 0.01))
            sample = math.sin(phase) + 0.55 * math.sin(2.01 * phase) + 0.25 * math.sin(3.98 * phase)
        elif voice == "bass":
            sample = math.sin(phase) + 0.18 * math.sin(2 * phase)
        elif voice == "pad":
            slow_attack = min(1.0, t / 0.35)
            slow_release = min(1.0, (duration - t) / 0.35)
            envelope = max(0.0, slow_attack * slow_release)
            sample = math.sin(phase) + 0.22 * math.sin(phase * 1.005) + 0.16 * math.sin(2 * phase)
        elif voice == "square":
            sample = 1.0 if math.sin(phase) >= 0 else -1.0
            envelope *= math.exp(-4.0 * t / max(duration, 0.01))
        else:
            sample = math.sin(phase)

        buf[begin + i] += volume * envelope * sample


def add_noise(buf, start, duration, volume, seed=0):
    rng = random.Random(seed)
    begin = int(start * SR)
    length = min(int(duration * SR), len(buf) - begin)
    for i in range(max(0, length)):
        t = i / SR
        envelope = math.exp(-28.0 * t)
        buf[begin + i] += volume * envelope * (rng.random() * 2.0 - 1.0)


def normalize_and_write(path, buf, peak=0.86):
    maximum = max(0.001, max(abs(i) for i in buf))
    scale = peak / maximum
    pcm = array("h", (int(max(-1.0, min(1.0, sample * scale)) * 32767) for sample in buf))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with wave.open(path, "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(SR)
        output.writeframes(pcm.tobytes())


def make_music(path, bpm, chords, melody, mood):
    beat = 60.0 / bpm
    bars = len(chords)
    duration = bars * 4 * beat
    buf = array("f", [0.0]) * int(duration * SR)

    for bar, chord in enumerate(chords):
        start = bar * 4 * beat
        root, third, fifth, top = chord
        for note in chord:
            add_tone(buf, start, 4 * beat, note, 0.045 if mood != "tension" else 0.035, "pad")
        for pulse in range(4):
            add_tone(buf, start + pulse * beat, beat * 0.82, root - 12, 0.13, "bass")
        pattern = (root, fifth, third, top, fifth, third, top, fifth)
        for step, note in enumerate(pattern):
            add_tone(buf, start + step * beat / 2, beat * 0.42, note + 12, 0.075, "piano")
        if mood == "campus":
            for pulse in (1, 3):
                add_noise(buf, start + pulse * beat, 0.10, 0.025, bar * 10 + pulse)
        elif mood == "oracle":
            for step in range(8):
                add_tone(buf, start + step * beat / 2, beat * 0.20, top + 12, 0.028, "bell")
        else:
            add_tone(buf, start, 4 * beat, root - 24, 0.055, "bass")

    for beat_index, note, beats in melody:
        add_tone(buf, beat_index * beat, beats * beat * 0.92, note, 0.12, "bell" if mood == "oracle" else "piano")

    normalize_and_write(path, buf)


def make_sfx(path, duration, notes, noise=None):
    buf = array("f", [0.0]) * int(duration * SR)
    for start, length, note, volume, voice in notes:
        add_tone(buf, start, length, note, volume, voice)
    if noise:
        for start, length, volume, seed in noise:
            add_noise(buf, start, length, volume, seed)
    normalize_and_write(path, buf, peak=0.80)


def main():
    make_music(
        os.path.join(BGM_DIR, "campus_afterglow.wav"),
        92,
        [(60, 64, 67, 71), (57, 60, 64, 69), (53, 57, 60, 64), (55, 59, 62, 67)] * 2,
        [(0, 72, 1), (2, 76, 1), (4, 79, 2), (8, 76, 1), (10, 74, 1), (12, 72, 2),
         (16, 69, 1), (18, 72, 1), (20, 76, 2), (24, 74, 1), (26, 71, 1), (28, 72, 2)],
        "campus",
    )
    make_music(
        os.path.join(BGM_DIR, "math_oracle.wav"),
        120,
        [(62, 66, 69, 74), (64, 67, 71, 76), (59, 62, 66, 71), (61, 64, 68, 73)] * 2,
        [(0, 86, 0.5), (1, 81, 0.5), (2, 83, 0.5), (3, 78, 0.5), (4, 81, 1),
         (8, 88, 0.5), (9, 83, 0.5), (10, 85, 0.5), (11, 80, 0.5), (12, 83, 1),
         (16, 86, 0.5), (18, 90, 0.5), (20, 88, 1), (24, 85, 0.5), (26, 83, 0.5), (28, 86, 2)],
        "oracle",
    )
    make_music(
        os.path.join(BGM_DIR, "dusk_tension.wav"),
        72,
        [(57, 60, 64, 69), (53, 57, 60, 65), (55, 58, 62, 67), (52, 56, 59, 64)] * 2,
        [(0, 69, 2), (4, 68, 2), (8, 65, 2), (12, 64, 2), (16, 69, 1), (18, 72, 1),
         (20, 68, 2), (24, 67, 1), (26, 64, 1), (28, 69, 2)],
        "tension",
    )

    make_sfx(os.path.join(SFX_DIR, "choice.wav"), 0.22, [(0, 0.16, 74, 0.45, "square"), (0.06, 0.14, 81, 0.35, "square")])
    make_sfx(os.path.join(SFX_DIR, "affection_up.wav"), 0.85, [(0, 0.5, 72, 0.42, "bell"), (0.12, 0.5, 76, 0.40, "bell"), (0.25, 0.55, 79, 0.38, "bell")])
    make_sfx(os.path.join(SFX_DIR, "affection_down.wav"), 0.70, [(0, 0.55, 61, 0.40, "square"), (0.16, 0.50, 56, 0.38, "square")])
    make_sfx(os.path.join(SFX_DIR, "event_unlock.wav"), 1.25, [(0, 0.8, 72, 0.36, "bell"), (0.16, 0.8, 79, 0.34, "bell"), (0.34, 0.85, 84, 0.34, "bell"), (0.52, 0.70, 88, 0.28, "bell")])
    make_sfx(os.path.join(SFX_DIR, "basketball.wav"), 0.55, [(0, 0.16, 43, 0.55, "bass"), (0.28, 0.14, 40, 0.40, "bass")], [(0, 0.08, 0.15, 42), (0.28, 0.07, 0.10, 43)])
    make_sfx(os.path.join(SFX_DIR, "school_bell.wav"), 2.1, [(0, 0.9, 79, 0.42, "bell"), (0.38, 0.9, 79, 0.40, "bell"), (0.9, 1.1, 76, 0.38, "bell")])
    make_sfx(os.path.join(SFX_DIR, "crab_power.wav"), 1.15, [(0, 0.8, 57, 0.32, "bass"), (0.1, 0.8, 69, 0.38, "bell"), (0.28, 0.75, 76, 0.34, "bell"), (0.45, 0.65, 81, 0.30, "bell")], [(0, 0.35, 0.08, 88)])


if __name__ == "__main__":
    main()
