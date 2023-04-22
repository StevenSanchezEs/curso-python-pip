import utils
import read_cvs
import charts

def run():
    data = read_cvs.read_csv('./data.csv')
    country = input('Type country => ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)

def run2():
    data = read_cvs.read_csv('./data.csv')

    if len(data) > 0:
        countries, percentages = utils.get_population_mundial(data)
        charts.generate_bar_chart(countries, percentages)

if __name__ == '__main__':
    run()
    run2()