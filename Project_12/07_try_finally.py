def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("I'm inside of finally")
        # Finally works whether try is succesfull or failed on function

main()