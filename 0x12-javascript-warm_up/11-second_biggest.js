#!/usr/bin/node

const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const nums = args.slice(2, args.length);
  nums.sort((a, b) => b - a);
  console.log(nums[1]);
}
