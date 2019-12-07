var costModel = {
    p1: 0,
    p2: 0,
    p3: 0,
    p4: 0,
    p5: 0,
    p6: 0,
    myCursorTime: 0,
    checkInterval: function (time, head, tail) { return time >= head && time <= tail; },
    interval1: function (cursorTime) { this.myCursorTime = 4; return 4 - cursorTime },
    interval2: function (cursorTime) { this.myCursorTime = 8; return 8 - cursorTime },
    interval3: function (cursorTime) { this.myCursorTime = 12; return 12 - cursorTime },
    interval4: function (cursorTime) { this.myCursorTime = 16; return 16 - cursorTime },
    interval5: function (cursorTime) { this.myCursorTime = 20; return 20 - cursorTime },
    interval6: function (cursorTime) { this.myCursorTime = 24; return 24 - cursorTime },
    getCost: function (startTime, endTime) {

        var start = parseInt(startTime.substring(0, 2)) + parseInt(startTime.substring(3, 5)) / 60;
        var end = parseInt(endTime.substring(0, 2)) + parseInt(endTime.substring(3, 5)) / 60;
        var deltaTime = end - start;
        var totalCost = 0;
        this.myCursorTime = start;

        if (this.myCursorTime > 0 && this.myCursorTime <= 4) { //interval1
            if (this.checkInterval(end, 0, 4)) {
                totalCost += this.p1 * (end - this.myCursorTime);
                this.myCursorTime = end;
            }
            else { totalCost += this.p1 * this.interval1(this.myCursorTime); }
        }
        if (this.myCursorTime >= 4 && this.myCursorTime <= 8) { //interval2
            if (this.checkInterval(end, 4, 8)) {
                totalCost += this.p2 * (end - this.myCursorTime);
                this.myCursorTime = end;
            }
            else { totalCost += this.p2 * this.interval2(this.myCursorTime); }
        }
        if (this.myCursorTime >= 8 && this.myCursorTime <= 12) { //interval3
            if (this.checkInterval(end, 8, 12)) {
                totalCost += this.p3 * (end - this.myCursorTime);
                this.myCursorTime = end;
            }
            else { totalCost += this.p3 * this.interval3(this.myCursorTime); }
        }
        if (this.myCursorTime >= 12 && this.myCursorTime <= 16) { //interval4
            if (this.checkInterval(end, 12, 16)) {
                totalCost += this.p4 * (end - this.myCursorTime);
                this.myCursorTime = end;
            }
            else { totalCost += this.p4 * this.interval4(this.myCursorTime); }
        }
        if (this.myCursorTime >= 16 && this.myCursorTime <= 20) { //interval5
            if (this.checkInterval(end, 16, 20)) {
                totalCost += this.p5 * (end - this.myCursorTime);
                this.myCursorTime = end;
            }
            else { totalCost += this.p5 * this.interval5(this.myCursorTime); }
        }
        if (this.myCursorTime >= 20 && this.myCursorTime <= 24) { //interval5
            if (this.checkInterval(end, 20, 24)) {
                totalCost += this.p6 * (end - this.myCursorTime);
                this.myCursorTime = end;
            }
            else { totalCost += this.p6 * this.interval6(this.myCursorTime); }
        }
        var final = totalCost.toPrecision(3);
        return parseFloat(final);

    },
    getNormalCostByShape: function (shape, start, end) {
        if (shape === 'car') {
            this.p1 = 1;
            this.p2 = 1.25;
            this.p3 = 2;
            this.p4 = 2;
            this.p5 = 2;
            this.p6 = 1.5;
            return this.getCost(start, end);

        }
        if (shape === 'truck') {
            this.p1 = 2.5;
            this.p2 = 2.75;
            this.p3 = 4;
            this.p4 = 4;
            this.p5 = 4;
            this.p6 = 3.5;
            return this.getCost(start, end);

        }

    },
    getWalkinCostByShape: function(shape, start, end){
        if (shape === 'car') {
            this.p1 = 2;
            this.p2 = 2.5;
            this.p3 = 3;
            this.p4 = 3;
            this.p5 = 2.75;
            this.p6 = 2.25;
            return this.getCost(start, end);

        }
        if (shape === 'truck') {
            this.p1 = 5;
            this.p2 = 5.5;
            this.p3 = 6;
            this.p4 = 6;
            this.p5 = 5.25;
            this.p6 = 4;
            return this.getCost(start, end);

        }

    }
}

module.exports = costModel;