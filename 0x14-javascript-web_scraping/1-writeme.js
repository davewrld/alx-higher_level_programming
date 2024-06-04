#!/usr/bin/node
const fs = require('fs);
fs.writeFile(process.argv['2'], 'uf8' function (error, content) {
	if (error) {
		console.error(error);
