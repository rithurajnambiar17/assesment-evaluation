var g = document.getElementsByClassName("group"),
    c = 0,
    i,
    v = false;

for (i = 0; i < g.length - 1; i++) {
    g[i].querySelector("input").onkeyup = g[i].querySelector("input").onchange = function() {
        if (this.validity.valid == true) {
            v = true;
            this.nextSibling.classList.add("valid");
        } else {
            v = false;
            this.nextSibling.classList.remove("valid");
        }
    };
    g[i].querySelector(".button").onclick = function() {
        if (v == true) {
            c++;
            this.parentNode.className = "group satu";
            this.parentNode.nextSibling.className = "group dua";
            document.querySelector(".progress").innerHTML =
                c +
                "/" +
                (g.length - 1) +
                " COMPLETED." +
                (c == g.length - 1
                    ? ""
                    : "");
            v = false;
        }
    };
}
