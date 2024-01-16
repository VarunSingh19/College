class Box1 {
    int l, h, w;

    Box1(int l1, int h1, int w1) {
        l = l1;
        h = h1;
        w = w1;
    }

    int getLength() {
        return l;
    }

    int getHeight() {
        return h;
    }

    int getWidth() {
        return w;
    }

    int getVolume() {
        return l * h * w;
    }
}

class BoxColor extends Box1 {
    int wt;
    BoxColor ob;

    BoxColor(String c, int l1, int h1, int w1){
        super(c,l1,h1,w1);
            w += w +1;
        
    }
}
class Third {
    public static void main(String[] args) {
        
    }
}
