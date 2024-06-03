
CC := gcc -O3
OBJ := gcc -O3 -c
DBG := gcc -g

OBJECTS := main.o

# all
all:
	echo "All dependencies gathered."

# main
main.o: main.c
	$(OBJ) -o $@ $<

main: main.o
	$(CC) -o $@ $^


# clean
clean:
	rm -f $(OBJECTS)
	rm -f $(basename $(OBJECTS))
	rm -f gmon.out

