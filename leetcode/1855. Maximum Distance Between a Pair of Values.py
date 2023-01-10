class Solution:
    def binary_search(self, arr: list[int], target: int, i: int):
        l, r = 0, len(arr) - 1
        mi = float('inf')
        index = 0
        if target == 8420:
            print()

        while l <= r:
            m = (l + r) // 2
            if m >= i and arr[m] >= target:
                mi = min(mi, arr[m])
                index = m
                l = m+1
            elif m < i:
                break
            elif arr[m] < target:
                r = m - 1
            else:
                l = m + 1
        return index - i

    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        m = float('-inf')
        nums2.append(m)
        for i, v in enumerate(nums1):
            if v == 8420:
                print()
            print(self.binary_search(nums2, v, i), v)
            m = max(m, self.binary_search(nums2, v, i))

        return m


a = Solution()
nums1 = [9999, 9998, 9997, 9997, 9996, 9996, 9994, 9994, 9994, 9993, 9992, 9989, 9987, 9985, 9983, 9983, 9982, 9981,
         9980, 9975, 9974, 9973, 9972, 9972, 9971, 9969, 9969, 9968, 9968, 9968, 9968, 9967, 9967, 9965, 9964, 9958,
         9958, 9957, 9957, 9956, 9955, 9954, 9952, 9952, 9951, 9950, 9949, 9948, 9948, 9947, 9943, 9941, 9941, 9935,
         9934, 9933, 9931, 9930, 9930, 9925, 9925, 9924, 9922, 9921, 9921, 9920, 9920, 9919, 9918, 9917, 9916, 9914,
         9914, 9914, 9913, 9912, 9912, 9908, 9906, 9906, 9903, 9901, 9900, 9897, 9897, 9895, 9895, 9894, 9893, 9892,
         9891, 9890, 9889, 9884, 9882, 9882, 9880, 9879, 9876, 9875, 9874, 9873, 9873, 9870, 9870, 9869, 9869, 9868,
         9864, 9863, 9862, 9861, 9861, 9860, 9860, 9859, 9857, 9856, 9855, 9855, 9852, 9852, 9849, 9849, 9847, 9847,
         9846, 9846, 9845, 9844, 9842, 9842, 9842, 9841, 9840, 9840, 9840, 9840, 9837, 9837, 9836, 9833, 9833, 9833,
         9831, 9831, 9829, 9828, 9827, 9824, 9823, 9823, 9821, 9820, 9820, 9819, 9819, 9818, 9816, 9815, 9813, 9813,
         9810, 9809, 9809, 9808, 9808, 9808, 9806, 9805, 9805, 9804, 9803, 9797, 9795, 9795, 9791, 9791, 9790, 9789,
         9789, 9789, 9788, 9788, 9786, 9783, 9782, 9782, 9780, 9780, 9777, 9776, 9775, 9774, 9773, 9771, 9769, 9767,
         9767, 9765, 9764, 9763, 9763, 9763, 9762, 9761, 9760, 9758, 9757, 9757, 9757, 9756, 9755, 9755, 9754, 9754,
         9750, 9746, 9745, 9745, 9744, 9742, 9741, 9739, 9739, 9736, 9734, 9733, 9733, 9731, 9730, 9729, 9727, 9725,
         9724, 9723, 9721, 9720, 9720, 9718, 9714, 9712, 9709, 9708, 9707, 9707, 9706, 9706, 9706, 9704, 9704, 9701,
         9700, 9700, 9700, 9700, 9697, 9696, 9693, 9692, 9692, 9692, 9691, 9691, 9689, 9686, 9684, 9683, 9681, 9681,
         9677, 9675, 9675, 9674, 9672, 9671, 9671, 9669, 9668, 9668, 9667, 9667, 9665, 9665, 9663, 9663, 9662, 9662,
         9662, 9662, 9661, 9658, 9658, 9656, 9655, 9654, 9653, 9653, 9651, 9651, 9651, 9651, 9649, 9648, 9647, 9647,
         9646, 9645, 9645, 9644, 9644, 9643, 9643, 9640, 9638, 9637, 9637, 9636, 9636, 9634, 9632, 9631, 9631, 9628,
         9622, 9621, 9618, 9617, 9615, 9614, 9613, 9613, 9612, 9611, 9611, 9611, 9609, 9609, 9606, 9606, 9605, 9605,
         9604, 9604, 9602, 9602, 9602, 9601, 9601, 9600, 9599, 9597, 9595, 9594, 9593, 9593, 9591, 9591, 9590, 9588,
         9585, 9580, 9578, 9578, 9578, 9573, 9572, 9572, 9570, 9568, 9563, 9563, 9560, 9560, 9559, 9558, 9556, 9555,
         9554, 9553, 9549, 9547, 9546, 9543, 9541, 9540, 9538, 9538, 9537, 9535, 9535, 9535, 9535, 9533, 9533, 9532,
         9532, 9530, 9530, 9527, 9525, 9524, 9522, 9521, 9521, 9519, 9518, 9516, 9515, 9515, 9513, 9512, 9508, 9507,
         9507, 9505, 9505, 9503, 9503, 9502, 9502, 9502, 9500, 9499, 9499, 9498, 9498, 9498, 9498, 9496, 9495, 9495,
         9494, 9493, 9493, 9493, 9491, 9491, 9489, 9489, 9489, 9486, 9486, 9485, 9485, 9484, 9484, 9483, 9483, 9479,
         9479, 9479, 9478, 9475, 9473, 9473, 9472, 9472, 9470, 9464, 9463, 9462, 9461, 9460, 9459, 9456, 9455, 9454,
         9454, 9453, 9452, 9452, 9452, 9451, 9450, 9447, 9446, 9443, 9443, 9442, 9441, 9440, 9439, 9437, 9437, 9437,
         9437, 9434, 9431, 9431, 9430, 9430, 9428, 9428, 9427, 9426, 9425, 9425, 9424, 9423, 9423, 9422, 9420, 9418,
         9416, 9416, 9415, 9415, 9414, 9412, 9412, 9411, 9409, 9406, 9405, 9405, 9404, 9404, 9403, 9403, 9403, 9403,
         9402, 9401, 9400, 9399, 9398, 9397, 9397, 9395, 9395, 9394, 9394, 9393, 9392, 9391, 9389, 9387, 9386, 9384,
         9382, 9381, 9381, 9380, 9379, 9377, 9376, 9375, 9374, 9373, 9371, 9368, 9366, 9365, 9365, 9365, 9363, 9363,
         9362, 9361, 9359, 9359, 9352, 9349, 9349, 9348, 9344, 9343, 9343, 9342, 9340, 9340, 9337, 9334, 9334, 9332,
         9331, 9331, 9331, 9329, 9329, 9328, 9328, 9326, 9321, 9319, 9318, 9317, 9316, 9316, 9315, 9315, 9314, 9314,
         9310, 9310, 9309, 9309, 9308, 9306, 9306, 9305, 9304, 9299, 9299, 9295, 9294, 9292, 9289, 9289, 9289, 9289,
         9288, 9288, 9286, 9286, 9285, 9285, 9285, 9285, 9284, 9284, 9283, 9282, 9282, 9281, 9278, 9278, 9277, 9276,
         9276, 9275, 9275, 9275, 9274, 9268, 9268, 9267, 9267, 9265, 9264, 9262, 9261, 9261, 9261, 9260, 9256, 9256,
         9255, 9254, 9252, 9252, 9252, 9252, 9251, 9250, 9250, 9249, 9248, 9247, 9244, 9241, 9239, 9239, 9237, 9237,
         9237, 9236, 9233, 9233, 9232, 9232, 9232, 9229, 9229, 9227, 9226, 9226, 9225, 9225, 9221, 9221, 9221, 9220,
         9219, 9219, 9218, 9218, 9217, 9215, 9214, 9213, 9212, 9211, 9210, 9209, 9207, 9207, 9206, 9206, 9206, 9205,
         9204, 9203, 9202, 9201, 9200, 9198, 9194, 9194, 9192, 9192, 9190, 9190, 9188, 9187, 9186, 9186, 9186, 9183,
         9182, 9181, 9181, 9181, 9179, 9179, 9179, 9177, 9176, 9176, 9174, 9172, 9172, 9171, 9170, 9169, 9169, 9168,
         9167, 9167, 9166, 9166, 9165, 9165, 9159, 9154, 9153, 9153, 9151, 9151, 9150, 9147, 9145, 9144, 9144, 9142,
         9142, 9142, 9141, 9139, 9138, 9138, 9134, 9133, 9133, 9133, 9132, 9132, 9132, 9131, 9128, 9126, 9124, 9123,
         9123, 9122, 9121, 9121, 9119, 9118, 9116, 9116, 9115, 9115, 9114, 9112, 9111, 9111, 9109, 9108, 9107, 9105,
         9103, 9101, 9101, 9098, 9098, 9095, 9089, 9089, 9088, 9088, 9082, 9081, 9078, 9077, 9077, 9077, 9076, 9076,
         9074, 9073, 9072, 9071, 9067, 9067, 9066, 9066, 9065, 9065, 9064, 9063, 9063, 9062, 9059, 9056, 9054, 9054,
         9052, 9052, 9052, 9051, 9049, 9049, 9047, 9044, 9044, 9044, 9043, 9042, 9041, 9040, 9040, 9039, 9038, 9036,
         9036, 9035, 9032, 9032, 9031, 9029, 9028, 9026, 9026, 9026, 9026, 9025, 9023, 9022, 9020, 9017, 9016, 9015,
         9015, 9012, 9012, 9010, 9009, 9009, 9008, 9008, 9007, 9006, 9006, 9005, 9005, 9005, 9005, 9003, 9000, 8999,
         8998, 8995, 8995, 8994, 8994, 8993, 8992, 8991, 8991, 8990, 8988, 8988, 8987, 8984, 8982, 8982, 8980, 8979,
         8975, 8975, 8974, 8971, 8971, 8968, 8967, 8964, 8964, 8963, 8963, 8962, 8961, 8957, 8954, 8953, 8953, 8948,
         8948, 8945, 8941, 8941, 8940, 8940, 8939, 8938, 8936, 8935, 8934, 8932, 8931, 8930, 8929, 8929, 8929, 8928,
         8923, 8921, 8921, 8920, 8920, 8919, 8918, 8913, 8912, 8911, 8911, 8911, 8910, 8909, 8907, 8905, 8903, 8902,
         8902, 8901, 8899, 8898, 8898, 8897, 8896, 8895, 8894, 8894, 8892, 8890, 8890, 8889, 8888, 8888, 8887, 8885,
         8885, 8884, 8884, 8882, 8879, 8878, 8878, 8878, 8878, 8876, 8874, 8873, 8872, 8871, 8868, 8868, 8868, 8868,
         8867, 8867, 8866, 8866, 8862, 8861, 8860, 8859, 8859, 8859, 8857, 8856, 8854, 8853, 8851, 8846, 8846, 8845,
         8845, 8845, 8844, 8843, 8840, 8839, 8838, 8838, 8838, 8837, 8837, 8837, 8836, 8834, 8834, 8833, 8832, 8832,
         8824, 8823, 8823, 8820, 8819, 8818, 8818, 8817, 8816, 8816, 8816, 8816, 8816, 8815, 8810, 8810, 8809, 8808,
         8808, 8807, 8805, 8802, 8801, 8800, 8799, 8798, 8796, 8795, 8794, 8794, 8787, 8787, 8787, 8785, 8784, 8784,
         8784, 8783, 8782, 8781, 8780, 8778, 8778, 8777, 8777, 8774, 8771, 8769, 8769, 8769, 8769, 8767, 8767, 8767,
         8766, 8759, 8758, 8758, 8757, 8754, 8754, 8754, 8750, 8748, 8748, 8747, 8746, 8745, 8743, 8742, 8740, 8739,
         8739, 8737, 8737, 8733, 8732, 8731, 8731, 8729, 8723, 8723, 8722, 8720, 8718, 8718, 8717, 8716, 8712, 8712,
         8711, 8711, 8709, 8706, 8704, 8704, 8703, 8702, 8700, 8699, 8698, 8698, 8697, 8697, 8694, 8692, 8689, 8689,
         8688, 8687, 8686, 8685, 8684, 8684, 8684, 8683, 8682, 8681, 8679, 8678, 8678, 8672, 8659, 8656, 8654, 8653,
         8653, 8651, 8648, 8647, 8646, 8643, 8639, 8636, 8635, 8635, 8635, 8634, 8631, 8629, 8628, 8628, 8626, 8625,
         8620, 8619, 8616, 8616, 8615, 8614, 8614, 8614, 8613, 8613, 8612, 8610, 8608, 8608, 8607, 8606, 8603, 8602,
         8599, 8597, 8596, 8595, 8593, 8592, 8592, 8591, 8590, 8589, 8588, 8587, 8586, 8585, 8585, 8584, 8583, 8583,
         8582, 8582, 8581, 8580, 8579, 8576, 8576, 8575, 8575, 8574, 8573, 8572, 8571, 8571, 8569, 8568, 8567, 8565,
         8562, 8561, 8561, 8560, 8560, 8558, 8556, 8556, 8555, 8555, 8554, 8553, 8552, 8552, 8552, 8552, 8548, 8548,
         8547, 8545, 8543, 8543, 8542, 8542, 8542, 8540, 8540, 8538, 8538, 8536, 8535, 8533, 8530, 8530, 8529, 8526,
         8524, 8523, 8522, 8522, 8521, 8516, 8515, 8514, 8514, 8513, 8513, 8513, 8508, 8508, 8505, 8504, 8504, 8503,
         8501, 8500, 8498, 8496, 8496, 8496, 8492, 8492, 8488, 8487, 8487, 8486, 8486, 8485, 8483, 8482, 8482, 8481,
         8481, 8481, 8477, 8475, 8474, 8474, 8473, 8473, 8473, 8471, 8471, 8467, 8466, 8466, 8466, 8463, 8461, 8460,
         8458, 8456, 8454, 8452, 8451, 8451, 8448, 8448, 8446, 8446, 8445, 8445, 8443, 8443, 8443, 8441, 8437, 8436,
         8432, 8431, 8430, 8428, 8427, 8426, 8425, 8425, 8424, 8423, 8421, 8420, 8420, 8419, 8419, 8418, 8415, 8414,
         8413, 8413, 8412, 8412, 8412, 8409, 8405, 8404, 8404, 8404, 8403, 8403, 8402, 8399, 8399, 8398, 8397, 8395,
         8393, 8392, 8392, 8390, 8389, 8389, 8388, 8387, 8387, 8386, 8386, 8386, 8384, 8382, 8382, 8379, 8379, 8379,
         8378, 8378, 8377, 8376, 8375, 8374, 8374, 8372, 8372, 8371, 8370, 8369, 8369, 8367, 8365, 8365, 8364, 8362,
         8361, 8360, 8360, 8359, 8356, 8352, 8352, 8349, 8347, 8347, 8346, 8344, 8342, 8342, 8340, 8340, 8339, 8339,
         8338, 8338, 8337, 8336, 8336, 8336, 8334, 8334, 8332, 8332, 8331, 8331, 8330, 8328, 8328, 8325, 8325, 8324,
         8323, 8321, 8320, 8320, 8319, 8319, 8318, 8317, 8317, 8315, 8314, 8314, 8314, 8313, 8313, 8313, 8309, 8307,
         8307, 8307, 8305, 8304, 8304, 8304, 8303, 8294, 8294, 8293, 8293, 8291, 8290, 8288, 8288, 8287, 8286, 8286,
         8285, 8284, 8284, 8282, 8282, 8280, 8280, 8280, 8278, 8278, 8274, 8268, 8266]
nums2 = [10000, 10000, 10000, 9998, 9998, 9996, 9994, 9994, 9994, 9994, 9989, 9988, 9988, 9988, 9987, 9986, 9983, 9982,
         9980, 9980, 9980, 9980, 9980, 9978, 9978, 9978, 9976, 9974, 9974, 9972, 9971, 9970, 9970, 9970, 9969, 9967,
         9967, 9966, 9965, 9964, 9964, 9964, 9963, 9962, 9962, 9961, 9961, 9959, 9955, 9952, 9952, 9948, 9947, 9947,
         9946, 9945, 9944, 9944, 9944, 9943, 9942, 9941, 9940, 9939, 9939, 9938, 9936, 9935, 9935, 9934, 9933, 9930,
         9926, 9923, 9922, 9921, 9921, 9920, 9919, 9916, 9915, 9915, 9914, 9914, 9913, 9912, 9911, 9911, 9910, 9909,
         9905, 9904, 9902, 9902, 9900, 9899, 9897, 9897, 9892, 9892, 9891, 9891, 9889, 9888, 9886, 9885, 9885, 9883,
         9883, 9882, 9879, 9879, 9877, 9876, 9876, 9874, 9874, 9874, 9872, 9871, 9868, 9867, 9867, 9867, 9866, 9866,
         9863, 9863, 9862, 9862, 9861, 9860, 9859, 9859, 9856, 9855, 9855, 9853, 9852, 9852, 9850, 9850, 9847, 9847,
         9845, 9845, 9843, 9842, 9841, 9839, 9839, 9838, 9838, 9837, 9836, 9836, 9834, 9834, 9830, 9825, 9822, 9821,
         9821, 9818, 9818, 9816, 9814, 9814, 9813, 9813, 9812, 9812, 9812, 9811, 9810, 9810, 9810, 9810, 9809, 9809,
         9809, 9808, 9808, 9807, 9807, 9804, 9802, 9802, 9801, 9801, 9800, 9799, 9797, 9794, 9794, 9794, 9793, 9792,
         9791, 9791, 9790, 9789, 9788, 9788, 9787, 9787, 9786, 9784, 9784, 9783, 9783, 9782, 9782, 9780, 9776, 9774,
         9774, 9772, 9771, 9770, 9770, 9769, 9768, 9767, 9767, 9766, 9765, 9764, 9763, 9763, 9762, 9761, 9761, 9761,
         9760, 9758, 9758, 9758, 9756, 9753, 9751, 9750, 9750, 9750, 9748, 9744, 9744, 9743, 9742, 9741, 9741, 9740,
         9739, 9738, 9738, 9737, 9736, 9736, 9732, 9732, 9730, 9728, 9728, 9727, 9725, 9723, 9723, 9717, 9715, 9715,
         9714, 9712, 9712, 9712, 9711, 9710, 9710, 9710, 9707, 9703, 9702, 9701, 9700, 9700, 9698, 9696, 9693, 9693,
         9690, 9690, 9689, 9688, 9688, 9687, 9687, 9686, 9686, 9684, 9684, 9684, 9682, 9682, 9681, 9680, 9679, 9677,
         9677, 9675, 9674, 9672, 9671, 9670, 9670, 9670, 9668, 9668, 9668, 9668, 9666, 9665, 9665, 9664, 9662, 9662,
         9662, 9661, 9660, 9660, 9659, 9657, 9654, 9653, 9651, 9649, 9648, 9648, 9646, 9646, 9645, 9644, 9644, 9644,
         9644, 9643, 9641, 9641, 9641, 9640, 9640, 9639, 9639, 9636, 9636, 9635, 9635, 9634, 9633, 9632, 9631, 9630,
         9630, 9627, 9627, 9627, 9625, 9624, 9624, 9621, 9621, 9620, 9619, 9618, 9614, 9613, 9613, 9611, 9611, 9610,
         9609, 9608, 9606, 9606, 9606, 9606, 9606, 9603, 9601, 9599, 9599, 9598, 9598, 9593, 9590, 9590, 9590, 9589,
         9588, 9588, 9587, 9585, 9582, 9580, 9577, 9576, 9575, 9574, 9571, 9570, 9569, 9568, 9566, 9565, 9565, 9563,
         9561, 9561, 9560, 9558, 9558, 9557, 9556, 9554, 9552, 9552, 9552, 9552, 9551, 9550, 9550, 9549, 9548, 9546,
         9545, 9544, 9544, 9543, 9543, 9541, 9538, 9538, 9536, 9536, 9535, 9534, 9534, 9533, 9531, 9531, 9530, 9529,
         9529, 9528, 9528, 9526, 9523, 9523, 9521, 9520, 9520, 9520, 9517, 9517, 9517, 9516, 9516, 9516, 9515, 9512,
         9511, 9508, 9508, 9508, 9507, 9507, 9506, 9504, 9502, 9502, 9500, 9498, 9495, 9493, 9493, 9492, 9492, 9491,
         9490, 9490, 9490, 9489, 9489, 9488, 9484, 9483, 9483, 9482, 9481, 9480, 9479, 9477, 9476, 9476, 9476, 9474,
         9474, 9472, 9472, 9471, 9470, 9469, 9465, 9463, 9461, 9457, 9454, 9454, 9452, 9452, 9451, 9451, 9450, 9449,
         9444, 9442, 9442, 9439, 9438, 9438, 9437, 9436, 9436, 9435, 9435, 9435, 9434, 9434, 9434, 9432, 9432, 9431,
         9431, 9429, 9427, 9425, 9424, 9424, 9423, 9422, 9420, 9419, 9417, 9417, 9416, 9415, 9415, 9414, 9413, 9411,
         9410, 9408, 9408, 9408, 9407, 9406, 9404, 9402, 9401, 9401, 9399, 9398, 9395, 9394, 9393, 9393, 9391, 9391,
         9389, 9388, 9388, 9387, 9386, 9386, 9384, 9381, 9373, 9372, 9370, 9369, 9369, 9367, 9367, 9366, 9364, 9363,
         9363, 9362, 9361, 9361, 9359, 9359, 9358, 9357, 9357, 9355, 9352, 9351, 9351, 9351, 9350, 9350, 9350, 9348,
         9347, 9347, 9346, 9344, 9344, 9342, 9341, 9340, 9339, 9337, 9336, 9335, 9334, 9332, 9332, 9332, 9331, 9329,
         9328, 9327, 9327, 9326, 9326, 9326, 9325, 9324, 9324, 9323, 9323, 9323, 9321, 9319, 9319, 9313, 9313, 9313,
         9312, 9311, 9309, 9306, 9306, 9306, 9304, 9301, 9300, 9298, 9298, 9297, 9294, 9294, 9290, 9287, 9285, 9285,
         9284, 9284, 9283, 9283, 9281, 9281, 9280, 9280, 9280, 9280, 9279, 9278, 9274, 9273, 9272, 9272, 9271, 9270,
         9269, 9269, 9268, 9267, 9267, 9265, 9265, 9264, 9263, 9262, 9261, 9261, 9260, 9259, 9258, 9257, 9256, 9256,
         9255, 9255, 9254, 9254, 9253, 9251, 9250, 9248, 9246, 9246, 9246, 9245, 9245, 9243, 9243, 9242, 9242, 9240,
         9240, 9238, 9238, 9237, 9234, 9233, 9232, 9229, 9229, 9228, 9228, 9226, 9224, 9224, 9223, 9222, 9221, 9219,
         9216, 9214, 9214, 9213, 9210, 9209, 9209, 9209, 9205, 9205, 9204, 9200, 9200, 9200, 9199, 9199, 9198, 9197,
         9192, 9185, 9184, 9181, 9177, 9173, 9173, 9173, 9173, 9172, 9168, 9165, 9164, 9159, 9157, 9155, 9153, 9153,
         9153, 9153, 9153, 9152, 9150, 9148, 9146, 9146, 9146, 9145, 9144, 9144, 9142, 9142, 9140, 9139, 9138, 9137,
         9137, 9137, 9137, 9136, 9136, 9135, 9133, 9133, 9132, 9131, 9130, 9129, 9129, 9127, 9125, 9123, 9122, 9121,
         9121, 9121, 9120, 9119, 9118, 9118, 9115, 9115, 9113, 9113, 9110, 9109, 9108, 9108, 9106, 9106, 9105, 9104,
         9103, 9102, 9102, 9101, 9101, 9099, 9098, 9097, 9097, 9096, 9096, 9095, 9094, 9092, 9091, 9090, 9088, 9088,
         9088, 9087, 9087, 9086, 9085, 9085, 9084, 9083, 9082, 9082, 9079, 9079, 9075, 9074, 9073, 9073, 9070, 9069,
         9069, 9067, 9066, 9064, 9063, 9063, 9063, 9062, 9059, 9059, 9056, 9055, 9054, 9054, 9053, 9053, 9051, 9051,
         9050, 9050, 9049, 9047, 9043, 9042, 9041, 9038, 9037, 9034, 9034, 9032, 9032, 9029, 9029, 9028, 9027, 9026,
         9026, 9024, 9023, 9020, 9019, 9018, 9017, 9017, 9016, 9016, 9013, 9011, 9010, 9009, 9007, 9006, 9006, 9006,
         9003, 9001, 9000, 8997, 8996, 8996, 8994, 8994, 8993, 8992, 8992, 8990, 8989, 8987, 8983, 8983, 8981, 8980,
         8979, 8978, 8977, 8976, 8976, 8974, 8974, 8970, 8970, 8970, 8969, 8968, 8968, 8967, 8965, 8964, 8962, 8961,
         8956, 8955, 8954, 8953, 8952, 8945, 8944, 8944, 8943, 8943, 8941, 8940, 8940, 8939, 8936, 8933, 8933, 8933,
         8933, 8932, 8926, 8926, 8925, 8923, 8923, 8921, 8920, 8919, 8918, 8917, 8916, 8916, 8916, 8915, 8914, 8913,
         8912, 8912, 8912, 8910, 8909, 8908, 8907, 8905, 8903, 8902, 8902, 8902, 8900, 8900, 8899, 8898, 8898, 8897,
         8896, 8894, 8893, 8893, 8893, 8892, 8892, 8891, 8891, 8891, 8887, 8886, 8886, 8885, 8882, 8881, 8879, 8877,
         8876, 8875, 8875, 8873, 8873, 8871, 8867, 8864, 8862, 8862, 8862, 8861, 8858, 8858, 8856, 8856, 8855, 8854,
         8853, 8852, 8852, 8851, 8849, 8849, 8848, 8848, 8843, 8842, 8840, 8836, 8836, 8834, 8832, 8832, 8832, 8832,
         8832, 8832, 8831, 8830, 8828, 8826, 8826, 8825, 8825, 8824, 8822, 8822, 8821, 8821, 8820, 8820, 8818, 8817,
         8817, 8816, 8816, 8815, 8815, 8814, 8814, 8813, 8812, 8811, 8810, 8809, 8806, 8805, 8800, 8797, 8797, 8797,
         8796, 8796, 8796, 8793, 8790, 8786, 8785, 8780, 8779, 8778, 8777, 8777, 8772, 8771, 8771, 8769, 8768, 8767,
         8767, 8766, 8766, 8763, 8762, 8760, 8759, 8755, 8754, 8754, 8753, 8753, 8753, 8752, 8752, 8751, 8751, 8750,
         8748, 8746, 8745, 8745, 8745, 8743, 8743, 8742, 8739, 8737, 8737, 8737, 8730, 8730, 8727, 8726, 8724, 8723,
         8722, 8722, 8722, 8721, 8720, 8720, 8718, 8714, 8714, 8712, 8712, 8711, 8707, 8707, 8704, 8704, 8703, 8700,
         8698, 8696, 8695, 8693, 8693, 8692, 8692, 8689, 8689, 8689, 8686, 8684, 8683, 8681, 8675, 8675, 8673, 8672,
         8671, 8668, 8667, 8666, 8666, 8665, 8663, 8662, 8660, 8660, 8659, 8658, 8658, 8658, 8657, 8655, 8655, 8655,
         8654, 8653, 8653, 8650, 8649, 8649, 8645, 8642, 8641, 8641, 8639, 8637, 8635, 8634, 8634, 8633, 8629, 8628,
         8627, 8626, 8623, 8623, 8622, 8620, 8620, 8620, 8620, 8619, 8615, 8614, 8612, 8612, 8612, 8611, 8610, 8610,
         8609, 8608, 8605, 8604, 8604, 8602, 8600, 8600, 8599, 8598, 8596, 8596, 8596, 8594, 8592, 8592, 8591, 8590,
         8589, 8589, 8588, 8587, 8587, 8586, 8585, 8585, 8584, 8583, 8578, 8576, 8575, 8575, 8574, 8574, 8572, 8572,
         8571, 8569, 8567, 8567, 8565, 8561, 8560, 8560, 8560, 8558, 8558, 8557, 8556, 8555, 8555, 8554, 8554, 8553,
         8549, 8547, 8547, 8545, 8544, 8542, 8542, 8542, 8542, 8541, 8541, 8539, 8538, 8534, 8534, 8530, 8530, 8529,
         8526, 8526, 8526, 8526, 8525, 8524, 8521, 8520, 8518, 8517, 8511, 8509, 8508, 8507, 8507, 8505, 8503, 8502,
         8502, 8501, 8500, 8500, 8500, 8500, 8499, 8496, 8496, 8495, 8494, 8494, 8493, 8491, 8490, 8489, 8489, 8488,
         8487, 8487, 8486, 8485, 8485, 8484, 8484, 8483, 8482, 8481, 8479, 8479, 8479, 8479, 8478, 8478, 8477, 8476,
         8475, 8475, 8474, 8473, 8470, 8469, 8468, 8466, 8462, 8462, 8458, 8457, 8454, 8454, 8453, 8453, 8453, 8452,
         8450, 8450, 8449, 8448, 8447, 8447, 8447, 8445, 8445, 8443, 8439, 8437, 8437, 8435, 8435, 8434, 8432, 8432,
         8431, 8430, 8429, 8426, 8425, 8424, 8423, 8422, 8422, 8421, 8421, 8420, 8420, 8420, 8415, 8414, 8412, 8410,
         8410, 8409, 8408, 8408, 8406, 8406, 8405, 8403, 8402, 8402, 8401, 8401, 8400, 8397, 8397, 8397, 8395, 8395,
         8389, 8389, 8389, 8387, 8386, 8385, 8381, 8377, 8376, 8373, 8371, 8371, 8371, 8370, 8369, 8369, 8368, 8367,
         8367, 8365, 8364, 8361, 8360, 8359, 8358, 8357, 8356, 8354, 8354, 8353, 8352, 8352, 8350, 8349, 8349, 8348,
         8348, 8347, 8343, 8343, 8342, 8342, 8340, 8337, 8336, 8335, 8333, 8333]

print(a.maxDistance(nums1=nums1, nums2=nums2))