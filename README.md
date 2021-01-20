node-x22i
===============
NodeJS Binding for x22i hashing algorithm

Current version v1.0.0
Usage
-------
```js
var x22i = require('node-x22i');
var buf = Buffer.from('password', 'utf8');
var hash = x22i.x22i(buf);
console.log(hash);
// => <Buffer cb 78 00 4e 36 14 56 0b c1 98 cd e0 5b 17 a5 06 13 7c ac 77 5a cf e0 fc 4e e2 cf 23 30 54 2a 17>
