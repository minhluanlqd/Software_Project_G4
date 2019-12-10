module.exports = (temp , username) => {
    let output = temp.replace(/{%USERNAME%}/g, username);
    return output;
  }