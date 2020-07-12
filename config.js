let define = (name,val) => {
	Object.defineProperty(exports,name, {
		value: val,
		enumerable: true
	});
};

define('AP_API_KEY','YOUR_API_KEY')
define('AP_API_SECRET','YOUR_SECRET_KEY')
//define('AV_API_KEY','YOUR_API_KEY')
