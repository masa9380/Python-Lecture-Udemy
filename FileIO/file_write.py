with open('writing_file.txt', mode='w') as f:
    f.write("You can write contents here\nuse 'backslash' to break the row")
    f.write("new write() doesn't break row\n")
    # mode='w'の場合は、truncatedされる：byte=0すなわちデータが一旦全て消える
    print("You can add a new row using 'file' parameter", file=f)
    print("new print() method breaks the row for you!", file=f)