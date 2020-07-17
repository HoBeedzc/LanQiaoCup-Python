def extend(n):
    draw[0] = '$$$' + draw[0][1:-1] + '$$$'
    draw[-1] = '$$$' + draw[-1][1:-1] + '$$$'
    for i in range(1,len(draw)-1):
        draw[i] = '$.' + draw[i] + '.$'
    draw.insert(0,'..$'+'.'*(4*n-1)+'$..')
    draw.insert(0,'..'+'$'*(4*n+1)+'..')
    draw.append('..$'+'.'*(4*n-1)+'$..')
    draw.append('..'+'$'*(4*n+1)+'..')

def show():
    for item in draw:
        print(item)

n = int(input())
draw = ['..$$$$$..',
        '..$...$..',
        '$$$.$.$$$',
        '$...$...$',
        '$.$$$$$.$',
        '$...$...$',
        '$$$.$.$$$',
        '..$...$..',
        '..$$$$$..']
for i in range(2,n+1):
    extend(i)
show()