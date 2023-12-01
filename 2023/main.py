import os
import sys

if __name__ == "__main__":
    match sys.argv[1]:
        case "init":
            day = sys.argv[2]
            # TODO get data from api
            os.system(f"mkdir {day}")
            os.system(f"touch {day}/input.txt")
            os.system(f"touch {day}/A.output")
            os.system(f"touch {day}/B.output")
            os.system(f"touch {day}/A.py")
            os.system(f"touch {day}/B.py")

        case "run":
            day = sys.argv[2]
            exercise = sys.argv[3]
            assert exercise in ["A", "B"]
            os.system(f"python3 {day}/{exercise}.py < {day}/input.txt > {day}/{exercise}.output")
            with open(f"{day}/{exercise}.output") as output:
                print(output.read())

        # TODO case "submit"