
var garage = {
    floor1: [true, true, true, true, true],
    floor2: [true, true, true, true, true],
    floor3: [true, true, true, true, true],
    floor4: [true, true, true, true, true],
    floor5: [true, true, true, true, true],

    /*floor1: [false, false, false, false, false],
    floor2: [false, false, false, false, false],
    floor3: [false, false, false, false, false],
    floor4: [false, false, false, false, false],
    floor5: [false, false, false, false, false],*/ 





    getSlotNumber: function (floor, order) {
        return floor * 100 + order;

    },

    isEmptySlot: function (slotNum) {
        var order = slotNum % 10;
        var floor = parseInt(slotNum / 100);
        if (floor === 1) return this.floor1[order - 1];
        if (floor === 2) return this.floor2[order - 1];
        if (floor === 3) return this.floor3[order - 1];
        if (floor === 4) return this.floor4[order - 1];
        if (floor === 5) return this.floor5[order - 1];

    },

    remainSlot: function (shape) {
        if (shape === 'truck')
            return this.isEmptySlot(103) || this.isEmptySlot(104) || this.isEmptySlot(105) ||
                this.isEmptySlot(203) || this.isEmptySlot(204) || this.isEmptySlot(205) ||
                this.isEmptySlot(303) || this.isEmptySlot(304) || this.isEmptySlot(305) ||
                this.isEmptySlot(403) || this.isEmptySlot(404) || this.isEmptySlot(405) ||
                this.isEmptySlot(503) || this.isEmptySlot(504) || this.isEmptySlot(505);

        if (shape === 'car') {
            return this.isEmptySlot(101) || this.isEmptySlot(102) ||
                this.isEmptySlot(201) || this.isEmptySlot(202) ||
                this.isEmptySlot(301) || this.isEmptySlot(302) ||
                this.isEmptySlot(401) || this.isEmptySlot(402) ||
                this.isEmptySlot(501) || this.isEmptySlot(502);

        }

    },

    fillSlot: function (floor, order) {
        if (floor === 1) this.floor1[order - 1] = false;
        if (floor === 2) this.floor2[order - 1] = false;
        if (floor === 3) this.floor3[order - 1] = false;
        if (floor === 4) this.floor4[order - 1] = false;
        if (floor === 5) this.floor5[order - 1] = false;
    },

    releaseSlot: function (slotNum) {
        var order = slotNum % 10;
        var floor = parseInt(slotNum / 100);
        if (floor === 1) this.floor1[order - 1] = true;
        if (floor === 2) this.floor2[order - 1] = true;
        if (floor === 3) this.floor3[order - 1] = true;
        if (floor === 4) this.floor4[order - 1] = true;
        if (floor === 5) this.floor5[order - 1] = true;

    },

    assignSlot: function (shape) {
        if (!this.remainSlot(shape)) return console.log('no more slot for ' + shape);

        else {
            for (let floor = 1; floor <= 5; floor++) {
                if (shape === 'car') {
                    for (let order = 1; order <= 2; order++)
                        if (this.isEmptySlot(this.getSlotNumber(floor, order))) {
                            this.fillSlot(floor, order);
                            return this.getSlotNumber(floor, order);

                        }
                }

                if (shape === 'truck') {
                    for (let order = 3; order <= 5; order++)
                        if (this.isEmptySlot(this.getSlotNumber(floor, order))) {
                            this.fillSlot(floor, order);
                            return this.getSlotNumber(floor, order);
                        }
                }


            }

        }

    }

};

module.exports = garage;







































