#   101	100	99	98	97	96	95	94	93	92	91
#   102	65	64	63	62	61	60	59	58	57	90
#   103	66	37	36	35	34	33	32	31	56	89
#   104	67	38	17	16	15	14	13	30	55	88
#   105	68	39	18	5	4	3	12	29	54	87
#   106	69	40	19	6	1	2	11	28	53	86
#   107	70	41	20	7	8	9	10	27	52	85
#   108	71	42	21	22	23	24	25	26	51	84
#   109	72	43	44	45	46	47	48	49	50	83
#   110	73	74	75	76	77	78	79	80	81	82
#   111	112	113	114	115	116	117	118	119	120	121


import math
CheckInput = 277678

SquareRoot = math.sqrt(CheckInput)

SquereRootLowRight = math.ceil(SquareRoot)

if  (SquereRootLowRight % 2) == 0:
    SquereRootLowRight +=1

SquereRootUpperLeft = SquereRootLowRight -1

RingNumber = math.ceil(SquereRootLowRight/2)

ValueLowerRight = SquereRootLowRight * SquereRootLowRight
ValueLowerLeft = ValueLowerRight - SquereRootUpperLeft
ValueUpperLeft = ValueLowerLeft - SquereRootUpperLeft
ValueUpperRight = ValueUpperLeft - SquereRootUpperLeft

OffsetMidle = SquereRootUpperLeft / 2

if CheckInput > ValueLowerLeft:
    print("Below")
    MiddleValue = ValueLowerLeft + OffsetMidle

elif CheckInput > ValueUpperLeft:
    print("Left")
    MiddleValue = ValueUpperLeft + OffsetMidle

elif CheckInput > ValueUpperRight:
    print("Top")
    MiddleValue = ValueUpperRight + OffsetMidle
else:
    print("Right")
    MiddleValue = ValueUpperRight - OffsetMidle

Steps = int( (RingNumber - 1) + (CheckInput - MiddleValue) )



print("MiddleValue = ", MiddleValue)
print("squarroot is ",SquareRoot)
print("SquereRootLowRight is ", SquereRootLowRight)
print("SquereRootUpperLeft is ", SquereRootUpperLeft)
print("RingNumber is ", RingNumber)
print("ValueLowerRight is ", ValueLowerRight)
print("ValueLowerLeft is ", ValueLowerLeft)
print("ValueUpperLeft is ", ValueUpperLeft)
print("ValueUpperRight is ", ValueUpperRight)
print("Steps = ", Steps)
