"""
#   elif相当于JS中的 else if 适用于多个条件的判断
# 例如在JS中
#    var age = prompt("输入年龄：");
#    if ( age >= 60 ){
#	    alert("已经老了，好好享受剩下的岁月吧");
#    }else if( age >= 18 ){
#    	alert("你已经成年了");
#	}else if( age < 18 &&  age > 0){
#   		alert("你是未成年人");
#	}else{
#   		alert("请输入正确的年龄");
#	}
#
"""
# 在python中，上面的代码这样写：
age = int(input("输入年龄："))
if age >= 60:
    print("已经老了，好好享受剩下的岁月吧")
elif age >= 18:
    print("你已经成年了")
elif 0 < age < 18:
    print("你是未成年人")
else:
    print("请输入正确的年龄")
