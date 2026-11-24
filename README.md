# The Funniest Sick-Day Excuse

[![make.fun](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/thanhvu261090/makefun-sick-day/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/thanhvu261090/makefun-sick-day/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

Entry for the [make.fun bounty "The Funniest Sick-Day Excuse"](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36): one line, under 200 characters, that someone could send to call in sick — the funniest excuse landed in one breath, half believable, and nothing else.

## The entry

> Can't come in today — I sneezed so hard I pulled a muscle, and now my back has filed a formal complaint, so I'm staying home to negotiate with it.

## How it works

`main.py` holds the excuse as a single string constant, validates it against the competition gate with `gate_check()` (UTF-8 text, 1–200 characters, not only whitespace, a single line), then writes it exactly as-is to `/output/entry.txt`.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
