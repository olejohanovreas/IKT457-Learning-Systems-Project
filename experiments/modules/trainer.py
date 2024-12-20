import numpy as np
from GraphTsetlinMachine.tm import MultiClassGraphTsetlinMachine
import plotly.graph_objects as go
from IPython.display import display


def train(graphs_train, labels_train, graphs_test, labels_test, dimensions, number_of_clauses, T, s, depth,
          accuracy_threshhold, epochs):
    tm = MultiClassGraphTsetlinMachine(
        number_of_clauses=number_of_clauses,
        T=T,
        s=s,
        depth=depth
    )


    train_accuracies = []
    test_accuracies = []
    max_train_accuracy = 0
    max_test_accuracy = 0

    fig = go.FigureWidget(
        data=[
            go.Scatter(x=[], y=[], mode='lines', name="Training Accuracy"),
            go.Scatter(x=[], y=[], mode='lines', name="Testing Accuracy"),
            go.Scatter(x=[], y=[], mode='lines', name="Test Regression", line=dict(dash='dash', color='gray'))
        ],
        layout=go.Layout(
            title=f"Training and Testing Accuracy, {dimensions}x{dimensions}",
            xaxis=dict(title="Epoch"),
            yaxis=dict(title="Accuracy"),
            annotations=[
                dict(text="Train: - , Test: -", x=0.5, y=1.2, xref="paper", yref="paper", showarrow=False,
                     font=dict(size=18)
                     )
            ]
        )
    )

    display(fig)

    for epoch in range(epochs):
        tm.fit(graphs_train, labels_train, 1, True)

        #evaluate on training data and testing data
        train_prediction = tm.predict(graphs_train)
        train_accuracy = (train_prediction == labels_train).mean()
        test_prediction = tm.predict(graphs_test)
        test_accuracy = (test_prediction == labels_test).mean()

        if train_accuracy > max_train_accuracy:
            max_train_accuracy = train_accuracy
        if test_accuracy > max_test_accuracy:
            max_test_accuracy = test_accuracy

        train_accuracies.append(train_accuracy)
        test_accuracies.append(test_accuracy)

        #compute regression line when more than one point
        x_data = np.arange(1, epoch + 2)
        if len(test_accuracies) > 1:
            coeffs = np.polyfit(x_data, test_accuracies, 1)
            test_poly = np.poly1d(coeffs)
            reg_y = test_poly(x_data)
        else:
            reg_y = [test_accuracies[0]]

        #update the plot
        with fig.batch_update():
            fig.data[0].x = list(range(1, epoch + 2))
            fig.data[0].y = train_accuracies
            fig.data[1].x = list(range(1, epoch + 2))
            fig.data[1].y = test_accuracies
            fig.data[2].x = x_data
            fig.data[2].y = reg_y

            fig.layout.annotations = [
                dict(
                    text=f"Train: {train_accuracy:.3f} (max: {max_train_accuracy:.3f}) , Test: {test_accuracy:.3f} (max: {max_test_accuracy:.3f})",
                    x=0.5,
                    y=1.2, xref="paper", yref="paper", showarrow=False, font=dict(size=18)
                )
            ]

            if test_accuracy >= accuracy_threshhold and train_accuracy >= accuracy_threshhold:
                break