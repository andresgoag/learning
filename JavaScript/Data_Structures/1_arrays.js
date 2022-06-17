class MyArray {
    constructor() {
        this.length = 0;
        this.data = {};
    }

    get(index) {
        return this.data[index];
    }

    push(item) {
        this.data[this.length] = item;
        this.length++;
        return this.data;
    }

    pop() {
        const lastItem = this.data[this.length - 1];
        delete this.data[this.lenght - 1];
        this.length--;
        return lastItem;
    }

    shiftIndex(index) {
        for (let i = index; i < this.length - 1; i++) {
            this.data[i] = this.data[i + 1];
        }
        delete this.data[this.length - 1];
        this.length--;
    }

    delete(index) {
        const item = this.data[index];
        this.shiftIndex(index);
        return item;
    }

    shift() {
        const item = this.data[0];
        this.delete(0);
        return item;
    }

    unshift(item) {
        for (let i = this.length; i > 0; i--) {
            this.data[i] = this.data[i - 1];
        }
        this.length++;
        this.data[0] = item;
        return this.data;
    }
}

const myArray = new MyArray();
