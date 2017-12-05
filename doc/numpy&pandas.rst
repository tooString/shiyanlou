=======
numpy
=======
- **ndarray**
  - ndarray.shape 数组信息
  - ndarray.size  数组元素个数
  - ndarray.dtype 数组存储元素类型
  - ndarray.ndim  数组的维数
  - ndarray.reshape() 变形为其他维数数组::

      a = np.arange(12)
       a1 = a.reshape(4, 3)
- **数组统计**
  - a.sum 计算多维数组的所有元素的和
  - a.max 最大值计算
  - a.min 最小值计算
  - a.mean 平均值计算
  - a.std 标准差计算
  - a.var 方差计算

  ::

    接收一个axis参数，用于指定统计哪根轴上的数据，
     axis=0 统计列，axis=1 统计行。
- **创建数组**
  - np.array()  创建普通数组
  - np.arange() 创建一维数组，类似Python内置range
  - np.ones()   创建元素值全为1的数组
  - np.zeros()  创建元素值全为0的数组
  - np.empty()  创建空值多维数组，只分配内存不填值
  - np.random.random  创建元素值为随机值得多维数组
  - np.sqrt     开方运算
  - np.dot      矩阵乘法
  - np.sort     排序
  - np.linalg   模块中包含了一些基本的线性代数计算函数

=======
pandas
=======
Series&DataFrame
----------------
- Series  一维数组，只有一个列和索引。索引可以定制::

    s = Series([1,2,3,4,5], index=['a','b','c','d','e'])
     s[0]    1
     s['a']  1
     s[0:3] == s['a':'c']
     a 1
     b 2
     c 3

  - 选择元素方式
    - 整数索引(默认存在)::

        s.iloc[0:3]
    - 指定字符索引::

        s.loc['a':'c']


- DataFrame 类似二维数组，有行和列之分，索引(行)标签(列)都可以被定制::

    df = DataFrame(np.random.randn(4, 4),
                   index=['a','b','c','d'],
                   columns=['A','B','C','D'])

  - 选择数据
    * 选择列::

       df.A
        df['A']
        df[df.columns[0:2]]
        df.loc[:,['A','B']]

    * 选择行::

        df.loc['a']
         df.loc['a':'c']
         df.iloc[0]
         df.iloc[0:3]

    * 二维选择::

        df.loc[:, ['B','C','D']]  选择三列
         df.loc['a':'c', 'A':'C']  选择三行三列

- 将函数应用到Series和DataFrame::

    f = lambda x: x.max() - x.min()
     df.apply(f)
     df.apply(f, axis=1)
     df.applymap(lambda x: x+1)
     Series可用 s.map方法

- 常用的统计
  - `count` 元素值的数量；
  - `mean` 平均值；
  - `std` 标准差；
  - `min` 最小值；
  - `25%` 下四分位数；
  - `50%` 中位数；
  - `75%` 上四分位数；
  - `max` 最大值；
  
- 数据的合并和分组
  - pandas.concat::

      pd.concat([df1, df2]) 类似数据库的join操作
  - pandas.merge::

      pd.merge(df1, df2)
  - group by::

      df[df['user_id'] == 5348]['minutes'].sum()
      df[['user_id', 'minutes']].groupby('user_id').sum()
