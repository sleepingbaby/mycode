def main():
    count = 0

    with open("345-0.txt", "r") as foo:
        with open("vamptracker.txt", "w") as bar:
            for line in foo:
                if "vampire" in line.lower():
                    print(line)
                    count += 1
                    bar.write(line)
    print(f"'vampire' appears {count} times")

if __name__ == "__main__":
    main()