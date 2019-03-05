
CC=g++

LIB_NAME = native_cpp
TARGET = ../${LIB_NAME}.so

CFLAGS = -fPIC -O0 -fno-inline -Wall -g    -I"/usr/include/python3.6m"

ODIR=obj


LIBS=-lm


_OBJ = ${LIB_NAME}.o 
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))


$(ODIR)/%.o: src/%.cpp
	$(CC) -c -o $@ $< $(CFLAGS)


.PHONY: all

all: build

build: ${TARGET}


${TARGET}: ${OBJ}
	$(CC) -o $@ -Wl,-h -Wl,$@ -shared -Wl,--start-group "${OBJ}"  -Wl,-Bstatic  -Wl,-Bdynamic -L/usr/local/lib -lboost_python36 -ldl -lpthread -lutil -Wl,--end-group -fPIC -g



.PHONY: clean

clean:
	rm -f $(ODIR)/*.o ${TARGET}