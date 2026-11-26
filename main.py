# Break Production, Own It — entry for make.fun
# One brutally honest line the instant the agent breaks production.
import os

LINE = "Postmortem: I ran the migration twice because the first run 'didn't feel like it worked'. It worked. Twice."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
