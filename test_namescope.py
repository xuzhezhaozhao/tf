import tensorflow as tf

with tf.name_scope("test_xxx"):
    c = tf.constant([1, 2, 3], name="nested")
    print c.op.name
