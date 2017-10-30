# JS

JS 数据类型：

​	数字、字符串、布尔、数组、对象、Null、Undefined

```javascript
for(var i=0; i<8; i++){
  document.write("number is "+i+"<br>");
}
```

```javascript
// 函数
function add(x, y){
    return x + y;
}

let add = function(x, y){
    return x + y;
}
// 匿名函数
[2，3，4，5].map(x => x**2);
(参数1, 参数2) => {
    语句1;
  	语句2;
};

```

```JavaScript
// 对象
// JS 的对象是可变的键值对集合
// 键名是合法的JS标识符并且不是JS的保留字，可以省略引号
var myObject = {
    'value' = 0,
  	'incrment': function(count){
    this.value += typeof count === 'number' ? count: 1;
	}
};
// 类
// 声明类的构造器
var Dog = function(name){
    this.name = name;
}
// 添加类方法
Dog.prototype.bark = function(){
    console.log('wang wang wang')
}
dog = new Dog('wc');
dog.bark();

// ES6 类
class Dog{
  	// 构造函数
    constructor(name){
      	// 属性
        this.name = name
    }
	// 方法
  	bark(){
        console.log('wang wang wang')
    }
}

```

