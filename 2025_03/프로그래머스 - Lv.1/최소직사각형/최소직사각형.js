function solution(sizes) {
  const reSizes = sizes.map(([garo, sero]) => garo < sero ? [sero, garo] : [garo, sero]);

  let [w, h] = [0, 0];
  reSizes.forEach(([garo, sero]) => {
    if(garo > w) w = garo;
    if(sero > h) h = sero;
  })
  return w*h;
}