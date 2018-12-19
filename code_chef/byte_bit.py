
population = {"bit": {"el_tm": 0, "ch_tm": 2, "total": 0}, "nibble": {"el_tm": 0, "ch_tm": 8, "total": 0},"byte": {"el_tm": 0, "ch_tm": 16, "total": 0}}

def update_pop(c_pop, el_tm):
	nw_bit = c_pop["bit"]["total"]
	nw_nibble = c_pop["nibble"]["total"]
	nw_byte = c_pop["byte"]["total"]
	c_pop["byte"]["el_tm"] = c_pop["byte"]["el_tm"] + el_tm
	if c_pop["byte"]["el_tm"] >= c_pop["byte"]["ch_tm"]:
		nw_bit = nw_bit + c_pop["byte"]["total"] * 2
		c_pop["byte"]["el_tm"] = c_pop["byte"]["el_tm"] - c_pop["byte"]["ch_tm"]

	c_pop["nibble"]["el_tm"] = c_pop["nibble"]["el_tm"] + el_tm
	if c_pop["nibble"]["el_tm"] >= c_pop["nibble"]["ch_tm"]:
		nw_bit = nw_bit + c_pop["nibble"]["total"] * 2
		c_pop["nibble"]["el_tm"] = c_pop["nibble"]["el_tm"] - c_pop["nibble"]["ch_tm"]

	c_pop["bit"]["el_tm"] = c_pop["bit"]["el_tm"] + el_tm
	if c_pop["bit"]["el_tm"] >= c_pop["bit"]["ch_tm"]:
		nw_bit = nw_bit + c_pop["bit"]["total"] * 2
		c_pop["bit"]["el_tm"] = c_pop["bit"]["el_tm"] - c_pop["bit"]["ch_tm"]


def get_population(time):
	c_pop = population

	if time <= 0:
		return [c_pop["bit"]["total"], c_pop["nibble"]["total"], c_pop["byte"]["total"]]

	rem_time = time
	while rem_time != 0:
		update_pop(c_pop, 1)
		rem_time = rem_time - 1

	return [c_pop["bit"]["total"], c_pop["nibble"]["total"], c_pop["byte"]["total"]]

if __name__ == "__main__":
	if argc < 3:
		return -1

